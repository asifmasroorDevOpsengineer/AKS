param ([int] $NUMBER_OF_JOBS)

if (-not (Test-Path "jmeter-jobs")) {
    mkdir jmeter-jobs
    write-host "Jobs directory has been created"
}


kubectl delete --ignore-not-found jobs -l jobgroup=jmeter

for ( $i = 0; $i -lt $NUMBER_OF_JOBS; $i++ ) {
    write-host "Submitting job $i"

    if (Test-Path ".\jmeter-jobs\job-$i.yaml") {
        rm ".\jmeter-jobs\job-$i.yaml"
    }

    ((Get-Content -path ".\jmeter-job-tmpl.yaml" -Raw) -replace '\$NO', $i) | Set-Content -Path ".\jmeter-jobs\job-$i.yaml"
    kubectl create -f .\jmeter-jobs\job-$i.yaml
    rm ".\jmeter-jobs\job-$i.yaml"
}

