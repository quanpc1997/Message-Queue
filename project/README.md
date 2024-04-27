export http_proxy=http://proxy.cyberspace.vn:3128
export https_proxy=http://proxy.cyberspace.vn:3128

docker run -it -p 8080:8080 -e DYNAMIC_CONFIG_ENABLED=true hub.vtcc.vn:8989/provectuslabs/kafka-ui