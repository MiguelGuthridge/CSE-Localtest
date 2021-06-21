#!/bin/python3

import argparse
import json
import sys
import os

import test, give, projectsetup
import localtestcommon as c

def badArgs():
    print(f"Run `localtest help` for help")
    exit()

def help():
    print('\n'.join([
        "localtest: A program so that you don't need to VLab anymore",
        "",
        "Commands:",
        " * help:     Display this message",
        " * setup:    Generate required files for using localtest with a project",
        "             and fetch starter code if necessary",
        "             Args:",
        "              * course: course code (eg 1511)",
        "              * project: project to start (eg lab01)",
        " * fetch:    Fetch starter code (use this after setting up a custom template)",
        " * instruct: Launch instructions for project in web browser",
        " * subs:     View course submissions in a web browser",
        " * test:     Run autotests on project",
        "             Args:",
        "              * exercises: specific exercises to test (defaults to all)",
        " * give:     Submit code from project",
        "             Args:",
        "              * exercises: specific exercises to submit (defaults to all)",
        " * upload:   Uploads the contents of the directory to VLab",
        " * update:   Runs a git pull to update the repository provided that it",
        "             was git cloned.",
        ""
        ]))
    print('\n'.join([
        "Notice: this program is provided in the hope that it will be useful,",
        "however, no guarantees are made that it will work correctly.",
        "This software is not endorsed by UNSW, and as such, you use it at your",
        "own risk. However, all feedback and contributions towards improving",
        "the software would be greatly appreciated.",
        ""
    ]))
    print(f"Version: {c.VERSION}")
    print(f"Setups library version: {c.SETUPS_VERSION}")
    print("Author: Miguel Guthridge")

def projecthelp():
    proj = c.getJson()
    try:
        c.launchURL(proj["help_url"])
    except KeyError:
        print(f"Error: help URL not found for this project ({proj['course']}_{proj['project']})")

def viewSubmissions():
    proj = c.getJson()
    c.viewSubmissions(proj["course"], c.UNSW_TERM)

def upload():
    usr, pwd = c.getZidPass()
    c.uploadFiles(usr, pwd, c.UPLOAD_FOLDER)

def update():
    print("Updating localtest...")
    os.chdir(os.path.dirname(__file__))
    os.system("git pull")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        badArgs()
    
    if sys.argv[1] == "test":
        test.main(sys.argv[2:])
    elif sys.argv[1] == "give":
        give.main(sys.argv[2:])
    elif sys.argv[1] == "setup":
        projectsetup.main(sys.argv[2:])
    elif sys.argv[1] == "fetch":
        projectsetup.mainFetch(sys.argv[2:])
    elif sys.argv[1] == "instruct":
        projecthelp()
    elif sys.argv[1] == "subs":
        viewSubmissions()
    elif sys.argv[1] == "help":
        help()
    elif sys.argv[1] == "upload":
        upload()
    elif sys.argv[1] == "update":
        update()
    else:
        badArgs()
