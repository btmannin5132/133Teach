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

## Publishing Octave like MATLAB

For ENGR 133, we have been asking students to publish their MATLAB scripts so we can see the outputs without having to run the scripts.  This may get removed at some point if our atuograder improves, but for now, this is still expected.  Octave does not have a designated publish option, so in order to print a similar document, we need to go about it a little differently.

1. Use this [octavePublish.m](/matlab/octavePublish.m) file in your prefered location.  (This does work in codespaces)
2. This file generates a .md, or markdown file, essentially a fancy text file.  In order to export it to a pdf, I reccomend using the 'Markdown PDF' by yzane' in VScode/codespaces
3. In the .m file, change the publisher to your name, and then make a struct type for each script/function you are publishing.  Each struct needs 4 pieces of information: 
  - 'target_file', string of the file you are trying to publish
  - 'args', list of arguments inputed.  This can be blank if it is a script, or an argumentless function
  - 'is_function', boolean of if this is a function or not
  - 'num_outputs', count of expected outputs
Nearly all of these are setup for functions, but still include if you are publishing a script, that way it can be all done with one file.
4. Execute the script, it should generate a .md file in the same directory as the publishing function
5. Use the markdown->pdf converter to make a pdf.