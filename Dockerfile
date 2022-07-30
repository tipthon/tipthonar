FROM tipthon/tipthonar:slim-buster

#clonning repo 
RUN git clone https://github.com/tipthon/tipthonar.git /root/tpthon
#working directory 
WORKDIR /root/tpthon

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/tpthon/bin:$PATH"

CMD ["python3","-m","tpthon"]
