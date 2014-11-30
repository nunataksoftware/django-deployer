from django.shortcuts import render
import subprocess
import git

import os

from django.conf import settings


def index(request):

    output = []

    # We update from our repoe
    try:
        g = git.cmd.Git(settings.BASE_DIR)
        output.append(
            {'command': 'git pull', 'output': g.pull(), 'status': 'success'})
    except Exception as e:
        output.append(
            {'command': 'git pull', 'output': str(e), 'status': 'error'})
        return render(request, 'deployer/index.html', {'output': output})
    # we install our modules

    use_standard_pip = True
    status = 'success'
    output_pip = "No output"

    try:
        import pip
    except Exception as e:
        output_pip = str(e) + " installing using an alternative method"

    else:
        subprocess.check_call(
            ["pip", 'install', '-r', os.path.join(settings.BASE_DIR, 'requirements.txt')])
        use_standard_pip = False
        output_pip = "Successfully installed requeriments.txt"

    if use_standard_pip:
        try:
            if pip.main(['install', '-r', os.path.join(settings.BASE_DIR, 'requirements.txt')]):
                output_pip = "Successfully installed requeriments.txt"
                status = 'success'
            else:
                output_pip = "There was a problem installing requeriments.txt"
                status = 'error'
        except Exception as e:
            output_pip = str(e)

    if status == 'error':
        return render(request, 'deployer/index.html', {'output': output})

    output.append({'command': 'pip install -r requirements.txt',
                   'output': output_pip, 'status': status})

    # we sync our database
    try:
        output.append({'command': 'python manage.py migrate', 'output': subprocess.check_output(
            ['python', os.path.join(settings.BASE_DIR, 'manage.py'), 'migrate']), 'status': 'success'})
    except Exception as e:
        output.append(
            {'command': 'python manage.py migrate', 'output': str(e), 'status': 'error'})
        return render(request, 'deployer/index.html', {'output': output})

    # restart our server
    if not settings.DEPLOYER_RESTART_SERVER:
        settings.DEPLOYER_RESTART_SERVER = ["touch", os.path.join(os.path.dirname(BASE_DIR), 'tmp', 'restart.txt')]
    try:
        subprocess.check_call(settings.DEPLOYER_RESTART_SERVER)
        output.append({'command': 'touch ' + os.path.join(os.path.dirname(settings.BASE_DIR),
                                                          'tmp', 'restart.txt'), 'output': 'Server restarted', 'status': 'success'})
    except Exception as e:
        output.append({'command': 'touch ' + os.path.join(os.path.dirname(settings.BASE_DIR),
                                                          'tmp', 'restart.txt'), 'output': str(e), 'status': 'error'})

    return render(request, 'deployer/index.html', {'output': output})
