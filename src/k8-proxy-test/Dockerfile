# Use a centos base image
FROM glasswallsolutions/k8-centos7:latest

# Install packages
RUN yum -y upgrade
RUN yum -y install wget
RUN yum -y install java-1.8.0-openjdk
RUN java -version
	
# # Install Taurus
# RUN pip3 install bzt    
# # Make Directories
# RUN mkdir -p /home/ubuntu/icap/input/ && \
#     mkdir -p /home/ubuntu/icap/output && \
#     mkdir -p /Test/Results/


# Set variables
ENV JMETER_HOME=/root/ \
    JMETER_VERSION=5.2.1 \
    TEST_SCRIPT_FILE=/Test/Proxy_Test.jmx \
    # HTML_REPORT=/Test/HTML_REPORT \
    TEST_LOG_FILE=/Test/test.log \
    TEST_RESULTS_PATH=/Test/Results/result.csv \
    URL_SOURCE=/Test/
    # ICAP_SCRIPT=/home/ubuntu/icap \
    # INPUT_FOLDER=/home/ubuntu/icap/input/ \
    # OUTPUT_FOLDER=/home/ubuntu/icap/output 
    
# Install Apache JMeter
RUN wget http://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz && \
    tar zxvf apache-jmeter-${JMETER_VERSION}.tgz && \
    rm -f apache-jmeter-${JMETER_VERSION}.tgz && \
    mv apache-jmeter-${JMETER_VERSION} ${JMETER_HOME}
RUN chmod +x ${JMETER_HOME}/apache-jmeter-5.2.1/bin
# Install Plugin Manager
# RUN cd /tmp/ &&\
#     wget -O jmeter-plugins-manager-1.4.jar http://search.maven.org/remotecontent?filepath=kg/apc/jmeter-plugins-manager/1.4/jmeter-plugins-manager-1.4.jar && \
#     wget -O cmdrunner-2.2.jar http://search.maven.org/remotecontent?filepath=kg/apc/cmdrunner/2.2/cmdrunner-2.2.jar && \
#     wget -O json-lib-2.4-jdk15.jar https://sourceforge.net/projects/json-lib/files/json-lib/json-lib-2.4/json-lib-2.4-jdk15.jar/download && \
#     mv /tmp/jmeter-plugins-manager-1.4.jar ${JMETER_HOME}/lib/ext/jmeter-plugins-manager-1.4.jar && \
#     mv /tmp/cmdrunner-2.2.jar ${JMETER_HOME}/lib/cmdrunner-2.2.jar &&\
#     mv /tmp/json-lib-2.4-jdk15.jar ${JMETER_HOME}/lib/json-lib-2.4-jdk15.jar &&\
#     java -cp ${JMETER_HOME}/lib/ext/jmeter-plugins-manager-1.4.jar org.jmeterplugins.repository.PluginManagerCMDInstaller && \
#     chmod +x ${JMETER_HOME}/bin/PluginsManagerCMD.sh &&\
#     ${JMETER_HOME}/bin/PluginsManagerCMD.sh install bzm-parallel=0.9 &&\
#     ${JMETER_HOME}/bin/PluginsManagerCMD.sh install jpgc-casutg=2.9

# Copy cert files
COPY assets-publishing-service-gov-uk.crt ${CERT_FILE}
# COPY script.sh ${ICAP_SCRIPT}
# RUN chmod +x ${ICAP_SCRIPT}
COPY Proxy_Test.jmx ${TEST_SCRIPT_FILE} 
RUN chmod +x ${TEST_SCRIPT_FILE} 
COPY inputpdf.csv ${URL_SOURCE}
#COPY xml_to_json.py ${CONVERT_JSON_PYTHON_SCRIPT}
#COPY upload_results.py ${UPLOAD_RESULTS_SCRIPT}
#COPY get_file_data.py ${GET_FILE_DATA_PYTHON_SCRIPT}

# Copy Test Data
# ADD testData ${INPUT_FOLDER}
# Enabling the system shared CA store
RUN update-ca-trust enable
RUN mv ${CERT_FILE}/assets-publishing-service-gov-uk.crt /etc/pki/ca-trust/source/anchors/assets-publishing-service-gov-uk.crt
RUN update-ca-trust extract

   
CMD ${JMETER_HOME}/apache-jmeter-5.2.1/bin/jmeter -n -t $TEST_SCRIPT_FILE -j $TEST_LOG_FILE -l $TEST_RESULTS_PATH
   
#CMD echo "\n\n===== RETRIEVING FILE DATA =====\n\n"    \
#    python3.7 $GET_FILE_DATA_PYTHON_SCRIPT -j $FILE_DATA_FILE -t $DYNAMODB_TEST_DATA_TABLE_NAME    \
#    echo "\n\n===== RUNNING TESTS =====\n\n"   \
#    $JMETER_HOME/bin/jmeter -n -t $TEST_SCRIPT_FILE -j $TEST_LOG_FILE  \
#    echo "\n\n===== TEST LOGS =====\n\n"   \
#    cat $TEST_LOG_FILE     \
#    echo "\n\n===== TEST RESULTS =====\n\n"    \
#    cat $TEST_RESULTS_PATH     \
#    echo "\n\n===== CONVERTING XML =====\n\n"  \
#    python3.7 $CONVERT_JSON_PYTHON_SCRIPT -i $TEST_RESULTS_PATH -o $TEST_RESULTS_JSON_PATH     \
#    echo "\n\n===== UPLOADING RESULTS =====\n\n"   \
#    python3.7 $UPLOAD_RESULTS_SCRIPT -j $TEST_RESULTS_JSON_PATH -t $DYNAMODB_RESULTS_TABLE_NAME    


