# Octave
Octave is an open source version of MATLAB that you can install on computers, inside of codespace, and run inside of VSCode.

Octave has the vast majority of the capabilites as MATLAB, but is much more light weight, and free.  There are a few functions that don't work quite the same way, but there are ways around the majority of them, especially for ENGR133.

## Installing Octave
Below are the steps to install Octave, and then run MATLAB scripts in VS Code.

Inside of the terminal (either in VS code, codespaces, or your local bash terminal):
```bash
sudo apt update
sudo apt install octave
```

You can then run octave in your terminal by running
```bash
octave
```
Running a file in Octave is the same as doing it with python, just with the Octave command instead. Go to the directory of the file, and run the script.
```
octave testScript.m
```
There are Octave extensions in VS code to help with color coding variables and whatnot if you like.

## If using Juypter Books (mainly for instructors)
In order to use Octave inside of JupyterBooks, you will need to install the octave kernel.

```
pip install octave_kernel
```
You can verify that the kernal was installed by running
```
jupyter kernelspec list
```
which should provide you with the different kernels available in your Jupyterbooks:
```
Available kernels:
  octave     /home/codespace/.local/share/jupyter/kernels/octave
  python3    /home/codespace/.local/share/jupyter/kernels/python3
```
After making your .ipynb file, and opening up a code section, select the Octave kernel from the kernel list. 