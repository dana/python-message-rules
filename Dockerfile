FROM centos

RUN yum install -y epel-release && yum -y update

RUN yum install -y python-distribute libcurl-devel 

RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | python2.7

RUN pip install six
RUN pip install message_match
RUN pip install message_transform
RUN pip install message_rules

ADD compile-rules.py /usr/bin
RUN mkdir /compile
WORKDIR /compile
CMD /usr/bin/compile-rules.py
