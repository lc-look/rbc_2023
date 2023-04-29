# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rbc_2023/UI2node.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class UI2node(genpy.Message):
  _md5sum = "3929c6344e36b839b0a0e74ac70b59cf"
  _type = "rbc_2023/UI2node"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 mode
bool isCheckShowWrite
bool isCheckShowRead
int32[] data"""
  __slots__ = ['mode','isCheckShowWrite','isCheckShowRead','data']
  _slot_types = ['int32','bool','bool','int32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       mode,isCheckShowWrite,isCheckShowRead,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(UI2node, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.mode is None:
        self.mode = 0
      if self.isCheckShowWrite is None:
        self.isCheckShowWrite = False
      if self.isCheckShowRead is None:
        self.isCheckShowRead = False
      if self.data is None:
        self.data = []
    else:
      self.mode = 0
      self.isCheckShowWrite = False
      self.isCheckShowRead = False
      self.data = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_i2B().pack(_x.mode, _x.isCheckShowWrite, _x.isCheckShowRead))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.mode, _x.isCheckShowWrite, _x.isCheckShowRead,) = _get_struct_i2B().unpack(str[start:end])
      self.isCheckShowWrite = bool(self.isCheckShowWrite)
      self.isCheckShowRead = bool(self.isCheckShowRead)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.data = s.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_i2B().pack(_x.mode, _x.isCheckShowWrite, _x.isCheckShowRead))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.data.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.mode, _x.isCheckShowWrite, _x.isCheckShowRead,) = _get_struct_i2B().unpack(str[start:end])
      self.isCheckShowWrite = bool(self.isCheckShowWrite)
      self.isCheckShowRead = bool(self.isCheckShowRead)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.data = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i2B = None
def _get_struct_i2B():
    global _struct_i2B
    if _struct_i2B is None:
        _struct_i2B = struct.Struct("<i2B")
    return _struct_i2B
