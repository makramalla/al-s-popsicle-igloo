NAME=als-popsicle-igloo
VERSION=0.0.1

prepare:
	./scripts/prepenv.sh

clean:
	rm -rf env/
	rm -rf export/server/
	rm -f export/*.json
	docker rm YANG-SWAGGER
	docker rmi swagger_server 

image-swagger:
	docker build -t swagger_server swagger/

image-netconf:
	docker build -t netconf_server -f netconf/Dockerfile .

image-grpc:
	ls

tag: image-swagger image-netconf image-grpc
	docker tag swagger_server:latest registry.blueplanet.com/ciena/als-popsicle-igloo/swagger_server:latest
	docker tag netconf_server:latest registry.blueplanet.com/ciena/als-popsicle-igloo/netconf_server:latest

tree:
	pyang -f tree YANG/als-popsicles-igloo.yang > YANG/als-popsicles-igloo.tree

yang-to-swagger:
	./scripts/create-swagger

yang-to-proto:
	ls

grpc-codegen:
	ls

swagger-codegen:
	docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -i /local/swagger/swagger-modified.json -l python-flask -o /local/swagger_codegen

start-swagger-server: image-swagger
	docker run --name YANG-SWAGGER -p 8080:8080 swagger_server

start-netconf-server: image-netconf
	docker run -d --rm -it --name netconf-server -p 830:830 netconf_server

push: tag
	docker push registry.blueplanet.com/ciena/als-popsicle-igloo/swagger_server:latest
	docker push registry.blueplanet.com/ciena/als-popsicle-igloo/netconf_server:latest
