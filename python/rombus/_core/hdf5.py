import h5py  # type: ignore

import rombus.exceptions as exceptions
from typing import TypeVar
from rombus._core.log import log

def ensure_open(file_in) -> h5py.File:
    try:
        if type(file_in) == Filename:
            return h5py.File(file_in, "r"), True
        elif type(file_in) == str:
            return file_in, False
        else:
            raise exceptions.RombusHDF5Error(
                f"An attempt to open an invalid type ({type(file_in)}) as an HDF5 file was encountered."
            )
    except (IOError, exceptions.RombusException) as e:
        log.handle_exception(e)
