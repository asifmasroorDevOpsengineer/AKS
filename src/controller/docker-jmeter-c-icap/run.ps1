param ([string] $CONFIG_FILE, [string] $FILES_LIST, [int] $NUMBER_OF_JOBS)

if (-not (Test-Path $CONFIG_FILE)) {
    write-host "Config file $($CONFIG_FILE) does not exist"
    exit
}

if (-not (Test-Path $FILES_LIST)) {
    write-host "Files list $($FILES_LIST) does not exist"
    exit
}

if (-not (Test-Path "jmeter-jobs")) {
    mkdir jmeter-jobs
    write-host "Jobs directory has been created"
}

if (Test-Path ".\files") {
    rm .\files
    write-host "Previous version of the file list has been removed"
}

if (Test-Path ".\jmeter-conf.jmx") {
    rm .\jmeter-conf.jmx
    write-host "Previous version of the JMX config file has been removed"
}

cp $CONFIG_FILE jmeter-conf.jmx
cp $FILES_LIST files

kubectl delete --ignore-not-found jobs -l jobgroup=jmeter
kubectl delete --ignore-not-found secret jmeterconf
kubectl delete --ignore-not-found secret filesconf
kubectl create secret generic jmeterconf --from-file=jmeter-conf.jmx
kubectl create secret generic filesconf --from-file=files

for ( $i = 0; $i -lt $NUMBER_OF_JOBS; $i++ ) {
    write-host "Submitting job $i"

    if (Test-Path ".\jmeter-jobs\job-$i.yaml") {
        rm ".\jmeter-jobs\job-$i.yaml"
    }

    ((Get-Content -path ".\jmeter-job-tmpl.yaml" -Raw) -replace '\$NO', $i) | Set-Content -Path ".\jmeter-jobs\job-$i.yaml"
    kubectl create -f .\jmeter-jobs\job-$i.yaml
    rm ".\jmeter-jobs\job-$i.yaml"
}

rm .\jmeter-conf.jmx
rm .\files
