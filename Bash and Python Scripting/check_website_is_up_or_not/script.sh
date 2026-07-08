#!/bin/bash

website=www.fakestoreapi.org

check_website(){
    status_code=$(curl --head -s "$website" |  awk '/^HTTP/{print $2}')
    if [[ "$status_code" == "200" || "$status_code" == "301" ]]; then
       echo 'website is up'
    else
       echo 'website is down'
    fi
}

check_website