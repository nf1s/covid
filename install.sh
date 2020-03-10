#!/usr/bin/env bash
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`


function JiraGitValidator {
	read -p "Would you like to install git branch and commit validators?: " yn

	case $yn in
		[Yy]* ) echo "Installing Jira ... " ;;
		[Nn]* ) echo "${red}skipping Jira validator ... ${reset}" ; return 0;;
		* ) echo "Please answer yes or no."; JiraGitValidator;
	esac

    echo "adding git validator configuration JSON ... "
    cp git_validator/.git-validator-config.json .

    echo "installing JIRA validator ... "
    cp git_validator/prepare-commit-msg .git/hooks
    chmod +x .git/hooks/prepare-commit-msg
    echo "${green} Jira validator successfully installed ... ${reset}"

}

function precommitHook {
    read -p "Would you like to install hooks for python (run black and flake8 before commit)?: " yn
	case $yn in
		[Yy]* ) echo "Installing pre-commit hooks ... " ;;
		[Nn]* ) echo "${red}skipping pre-commit hooks ... ${reset}" ; return 0;;
		* ) echo "Please answer yes or no.";precommitHook;
	esac

    echo "adding black configuration ... "
    cp git_validator/pyproject.toml .

    echo "adding flake8 configuration ... "
    cp git_validator/.flake8 .

    echo "adding pre-commit configuration ... "
    cp git_validator/.pre-commit-config.yaml .

    echo "installing pre-commit ... "
    pipenv install pre-commit --dev
    pipenv run pre-commit install

    echo "${green} pre-commit with (black and flake8) successfully installed ... ${reset}"

}


function main {
    echo "cloning git_validator ... "
    git clone https://github.com/hemdesignstudio/git_validator.git
    JiraGitValidator
    precommitHook
    rm -rf git_validator
    echo "removing git_validator ... "
    echo "${green}Done ... ${reset}"
}

main




