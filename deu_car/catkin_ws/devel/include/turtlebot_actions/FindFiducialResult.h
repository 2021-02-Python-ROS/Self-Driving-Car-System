// Generated by gencpp from file turtlebot_actions/FindFiducialResult.msg
// DO NOT EDIT!


#ifndef TURTLEBOT_ACTIONS_MESSAGE_FINDFIDUCIALRESULT_H
#define TURTLEBOT_ACTIONS_MESSAGE_FINDFIDUCIALRESULT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/PoseStamped.h>

namespace turtlebot_actions
{
template <class ContainerAllocator>
struct FindFiducialResult_
{
  typedef FindFiducialResult_<ContainerAllocator> Type;

  FindFiducialResult_()
    : pose()  {
    }
  FindFiducialResult_(const ContainerAllocator& _alloc)
    : pose(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::PoseStamped_<ContainerAllocator>  _pose_type;
  _pose_type pose;





  typedef boost::shared_ptr< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> const> ConstPtr;

}; // struct FindFiducialResult_

typedef ::turtlebot_actions::FindFiducialResult_<std::allocator<void> > FindFiducialResult;

typedef boost::shared_ptr< ::turtlebot_actions::FindFiducialResult > FindFiducialResultPtr;
typedef boost::shared_ptr< ::turtlebot_actions::FindFiducialResult const> FindFiducialResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator1> & lhs, const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator2> & rhs)
{
  return lhs.pose == rhs.pose;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator1> & lhs, const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace turtlebot_actions

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3f8930d968a3e84d471dff917bb1cdae";
  }

  static const char* value(const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3f8930d968a3e84dULL;
  static const uint64_t static_value2 = 0x471dff917bb1cdaeULL;
};

template<class ContainerAllocator>
struct DataType< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "turtlebot_actions/FindFiducialResult";
  }

  static const char* value(const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#result definition\n"
"geometry_msgs/PoseStamped pose\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/PoseStamped\n"
"# A Pose with reference coordinate frame and timestamp\n"
"Header header\n"
"Pose pose\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pose);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FindFiducialResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::turtlebot_actions::FindFiducialResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::turtlebot_actions::FindFiducialResult_<ContainerAllocator>& v)
  {
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::PoseStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TURTLEBOT_ACTIONS_MESSAGE_FINDFIDUCIALRESULT_H
