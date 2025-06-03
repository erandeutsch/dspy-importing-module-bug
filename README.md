# dspy-importing-module-bug

Minimal Python example reproducing a dspy module import/save bug.

## Update: Fixed in dspy 2.6.25!

With the new support for [custom imported module serialization with cloudpickle](https://github.com/stanfordnlp/dspy/pull/8286), this issue is now fixed! Any dspy programs that use imported signatures can be fixed in the following way:
```
import ExtractInfo
module = dspy.Predict(ExtractInfo.ExtractInfo)
module.save("testModule", save_program=True, modules_to_serialize=[ExtractInfo])
```

For more info, see the new [Serializing Imported Modules](https://dspy.ai/tutorials/saving/#:~:text=modules_to_serialize) section in the Saving and Loading tutorial.


## Overview

This repository demonstrates an issue when using the current version of dspy (2.6.24): a saved module cannot be reliably loaded from a different directory if it uses an imported signature from another file. 

By default, Cloudpickle does not serialize imported modules, and refers to them by reference. Due to this, a dspy program which uses an imported module which is saved in one directory, and loaded in a different directory, will not function properly. This leads to issues when transfering saved dspy programs across computers and repositories.


Usage
```bash
Clone the repository:
git clone https://github.com/erandeutsch/dspy-importing-module-bug.git
cd dspy-importing-module-bug
```

Install dependencies:
```bash
pip install dspy
```

Run saveDSPyExample.py to save the module, and the run loadDSPyExample.py to load the module

```bash
python folder1/saveDSPyExample.py
python loadDSPyExample.py
```

Resulting Behavior:
```bash
% python folder1/saveDSPyExample.py
Running the module directly in folder1:
Prediction(
    cityName='Paris[[ ## completed ## ]]'
)
Loading and running the module in folder1:
Prediction(
    cityName='Paris[[ ## completed ## ]]'
)

% python folder2/loadDSPyExample.py
Running the module directly in folder2:
Prediction(
    cityName='Paris[[ ## completed ## ]]'
)
Loading and running the module in folder2:
Traceback (most recent call last):
  File "/Users/eran/Documents/repositories/dspy-importing-module-bug/folder2/loadDSPyExample.py", line 17, in <module>
    loaded_module = dspy.load("testModule")
                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/eran/Documents/repositories/dspy-module-importing-fix/dspy/utils/saving.py", line 53, in load
    return cloudpickle.load(f)
           ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'ExtractInfo'
```

