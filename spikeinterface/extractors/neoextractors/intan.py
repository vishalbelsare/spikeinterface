import neo

from .neobaseextractor import NeoBaseRecordingExtractor, NeoBaseSortingExtractor


class IntanRecordingExtractor(NeoBaseRecordingExtractor):
    """
    Class for reading data from a intan board support rhd and rhs format.
    
    Based on neo.rawio.IntanRawIO
    
    Parameters
    ----------
    file_path: str
        
    stream_id: str or None
        
    """ 
    mode = 'file'
    NeoRawIOClass = 'IntanRawIO'
    
    def __init__(self, file_path, stream_id=None):
        neo_kwargs = {'filename' : str(file_path)}
        NeoBaseRecordingExtractor.__init__(self, stream_id=stream_id, **neo_kwargs)

def read_intan(*args, **kargs):
    recording = IntanRecordingExtractor(*args, **kargs)
    return recording
read_intan.__doc__ = IntanRecordingExtractor.__doc__