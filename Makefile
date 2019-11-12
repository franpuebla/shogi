help:
	@echo "Shogi-k8s"
	@echo "Docker"
	@echo "make build"
	@echo "make run"
	@echo "make kill"
	@echo ""
	@echo "Kubernetes"
	@echo "k8s-get"
	@echo "k8s-init"
	@echo "k8s-apply"
	@echo "k8s-delete"
	@echo "k8s-import"
	@echo "k8s-shell"

build:
	docker build --rm -t $(TAG) .

run:
	docker run -d --name $(TAG) --env-file $(ENV) -p $(LPORT):$(DPORT) $(TAG)

dev:
	docker run -it -v $(BASE_REPO):/opt/shogi --name $(TAG) --env-file $(ENV) -p $(LPORT):$(DPORT) $(TAG) ash

kill:
	docker kill $(TAG)
	docker rm $(TAG)

k8s-init:
	$(KBCTL) create secret generic $(K8STAG)-sec $(foreach var,$(shell cat ./Environment|xargs echo), --from-literal=$(var))
	$(KBCTL) get secret $(K8STAG)-sec -o yaml > $(K8STAG)-sec.yaml
	$(KBCTL) delete secret $(K8STAG)-sec

k8s-apply:
	$(KBCTL) apply -f .

k8s-shell:
	$(KBCTL) exec -it $(K8STAG)-0 ash

k8s-delete:
	$(KBCTL) delete -f .

k8s-get:
	$(KBCTL) get -f .


LPORT=8000
DPORT=8000
REPO=shogi
BASE_REPO=/Users/fran/Projects/shogi/src
#GIT=git@gitolite.itcx.loc
TAG=shogi
ENV=./Environment
KBCTL=kubectl --insecure-skip-tls-verify
K8STAG=shogi
SHELL := /bin/bash
include $(ENV)
