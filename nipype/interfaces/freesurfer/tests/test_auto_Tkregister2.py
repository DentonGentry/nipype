# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Tkregister2


def test_Tkregister2_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fsl_in_matrix=dict(argstr='--fsl %s',
    ),
    fsl_out=dict(argstr='--fslregout %s',
    ),
    fstal=dict(argstr='--fstal',
    xor=['target_image', 'moving_image'],
    ),
    fstarg=dict(argstr='--fstarg',
    xor=['target_image'],
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    moving_image=dict(argstr='--mov %s',
    mandatory=True,
    ),
    movscale=dict(argstr='--movscale %f',
    ),
    noedit=dict(argstr='--noedit',
    usedefault=True,
    ),
    reg_file=dict(argstr='--reg %s',
    mandatory=True,
    usedefault=True,
    ),
    reg_header=dict(argstr='--regheader',
    ),
    subject_id=dict(argstr='--s %s',
    ),
    subjects_dir=dict(),
    target_image=dict(argstr='--targ %s',
    xor=['fstarg'],
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    xfm=dict(argstr='--xfm %s',
    ),
    )
    inputs = Tkregister2.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Tkregister2_outputs():
    output_map = dict(fsl_file=dict(),
    reg_file=dict(),
    )
    outputs = Tkregister2.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
