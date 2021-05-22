$Env:CONDA_EXE = "/opt/Web/Conda/bin/conda"
$Env:_CE_M = ""
$Env:_CE_CONDA = ""
$Env:_CONDA_ROOT = "/opt/Web/Conda"
$Env:_CONDA_EXE = "/opt/Web/Conda/bin/conda"

Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1"
Add-CondaEnvironmentToPrompt