#!/bin/bash

_geckoPhoto()
{
    local path="$(dirname -- "${BASH_SOURCE[0]}")"
    local path="$(cd -- "$path" && pwd)"

    python3 $path/main.py
}

_geckoPhoto