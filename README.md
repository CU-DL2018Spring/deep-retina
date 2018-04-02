# deep retina
Deep retina is a project to test to what degree artificial neural networks can predict retinal ganglion cell responses to natural stimuli with high accuracy.

## Dependencies
```
$ pip install tableprint
$ conda install -c conda-forge deepdish
$ pip install pyret
```

## Getting started
1. Switch to the refactor branch. `git checkout refactor`
2. Activate your virtual environment.
3. Use tensorflow as backend. `export KERAS_BACKEND=tensorflow`
4. Run the bash script. `cd scripts; ./run_ln.sh`
