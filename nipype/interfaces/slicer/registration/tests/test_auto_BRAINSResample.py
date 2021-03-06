# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.registration.brainsresample import BRAINSResample

def test_BRAINSResample_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    defaultValue=dict(argstr='--defaultValue %f',
    ),
    deformationVolume=dict(argstr='--deformationVolume %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    gridSpacing=dict(argstr='--gridSpacing %s',
    sep=',',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='--inputVolume %s',
    ),
    interpolationMode=dict(argstr='--interpolationMode %s',
    ),
    inverseTransform=dict(argstr='--inverseTransform ',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    pixelType=dict(argstr='--pixelType %s',
    ),
    referenceVolume=dict(argstr='--referenceVolume %s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    warpTransform=dict(argstr='--warpTransform %s',
    ),
    )
    inputs = BRAINSResample.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_BRAINSResample_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = BRAINSResample.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

