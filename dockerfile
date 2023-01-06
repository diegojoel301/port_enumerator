FROM pwntools/pwntools
RUN sudo apt update
RUN sudo apt install net-tools
COPY ports.py /exploit/
