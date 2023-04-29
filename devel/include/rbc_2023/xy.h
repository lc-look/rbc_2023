// Generated by gencpp from file rbc_2023/xy.msg
// DO NOT EDIT!


#ifndef RBC_2023_MESSAGE_XY_H
#define RBC_2023_MESSAGE_XY_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rbc_2023
{
template <class ContainerAllocator>
struct xy_
{
  typedef xy_<ContainerAllocator> Type;

  xy_()
    : V()  {
    }
  xy_(const ContainerAllocator& _alloc)
    : V(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _V_type;
  _V_type V;





  typedef boost::shared_ptr< ::rbc_2023::xy_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rbc_2023::xy_<ContainerAllocator> const> ConstPtr;

}; // struct xy_

typedef ::rbc_2023::xy_<std::allocator<void> > xy;

typedef boost::shared_ptr< ::rbc_2023::xy > xyPtr;
typedef boost::shared_ptr< ::rbc_2023::xy const> xyConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rbc_2023::xy_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rbc_2023::xy_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rbc_2023::xy_<ContainerAllocator1> & lhs, const ::rbc_2023::xy_<ContainerAllocator2> & rhs)
{
  return lhs.V == rhs.V;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rbc_2023::xy_<ContainerAllocator1> & lhs, const ::rbc_2023::xy_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rbc_2023

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rbc_2023::xy_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rbc_2023::xy_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rbc_2023::xy_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rbc_2023::xy_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rbc_2023::xy_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rbc_2023::xy_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rbc_2023::xy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "18370905db842ff9f15c0610f2c0d8e2";
  }

  static const char* value(const ::rbc_2023::xy_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x18370905db842ff9ULL;
  static const uint64_t static_value2 = 0xf15c0610f2c0d8e2ULL;
};

template<class ContainerAllocator>
struct DataType< ::rbc_2023::xy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rbc_2023/xy";
  }

  static const char* value(const ::rbc_2023::xy_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rbc_2023::xy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string V\n"
;
  }

  static const char* value(const ::rbc_2023::xy_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rbc_2023::xy_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.V);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct xy_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rbc_2023::xy_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rbc_2023::xy_<ContainerAllocator>& v)
  {
    s << indent << "V: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.V);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RBC_2023_MESSAGE_XY_H
