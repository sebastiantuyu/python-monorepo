#########################################################################
#                                                                       #
#     Based from                                                        #
#     https://docs.aws.amazon.com/lambda/latest/dg/python-image.html    #
#                                                                       #
#########################################################################
FROM public.ecr.aws/lambda/python:3.8



###########################################
#                                         #
#   Install pyclk to handle the project   #
#                                         #
###########################################
RUN yum install -y unzip
RUN pip install pyyaml
RUN curl -LSs -O https://github.com/sebastiantuyu/pyclk/archive/refs/heads/main.zip
RUN unzip main.zip
RUN cd pyclk-main && python3 setup.py develop 
RUN pyclk version

###########################################
#                                         #
#       Copy & install the project        #
#                                         #
###########################################
ARG APP_NAME
COPY . ${LAMBDA_TASK_ROOT}

RUN ${LAMBDA_TASK_ROOT}/scripts/install
RUN pyclk install

CMD [ "/var/task/apps/lambda-dummy/app.handler" ]