; Auto-generated. Do not edit!


(cl:in-package deu_ros-srv)


;//! \htmlinclude TwoInts-request.msg.html

(cl:defclass <TwoInts-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:integer
    :initform 0)
   (b
    :reader b
    :initarg :b
    :type cl:integer
    :initform 0))
)

(cl:defclass TwoInts-request (<TwoInts-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TwoInts-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TwoInts-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name deu_ros-srv:<TwoInts-request> is deprecated: use deu_ros-srv:TwoInts-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <TwoInts-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deu_ros-srv:a-val is deprecated.  Use deu_ros-srv:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <TwoInts-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deu_ros-srv:b-val is deprecated.  Use deu_ros-srv:b instead.")
  (b m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TwoInts-request>) ostream)
  "Serializes a message object of type '<TwoInts-request>"
  (cl:let* ((signed (cl:slot-value msg 'a)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'b)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TwoInts-request>) istream)
  "Deserializes a message object of type '<TwoInts-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'a) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'b) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TwoInts-request>)))
  "Returns string type for a service object of type '<TwoInts-request>"
  "deu_ros/TwoIntsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TwoInts-request)))
  "Returns string type for a service object of type 'TwoInts-request"
  "deu_ros/TwoIntsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TwoInts-request>)))
  "Returns md5sum for a message object of type '<TwoInts-request>"
  "732182ffae20073c520fb831c7ee33cd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TwoInts-request)))
  "Returns md5sum for a message object of type 'TwoInts-request"
  "732182ffae20073c520fb831c7ee33cd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TwoInts-request>)))
  "Returns full string definition for message of type '<TwoInts-request>"
  (cl:format cl:nil "int32 a~%int32 b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TwoInts-request)))
  "Returns full string definition for message of type 'TwoInts-request"
  (cl:format cl:nil "int32 a~%int32 b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TwoInts-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TwoInts-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TwoInts-request
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
))
;//! \htmlinclude TwoInts-response.msg.html

(cl:defclass <TwoInts-response> (roslisp-msg-protocol:ros-message)
  ((result_add
    :reader result_add
    :initarg :result_add
    :type cl:integer
    :initform 0)
   (result_mult
    :reader result_mult
    :initarg :result_mult
    :type cl:integer
    :initform 0))
)

(cl:defclass TwoInts-response (<TwoInts-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TwoInts-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TwoInts-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name deu_ros-srv:<TwoInts-response> is deprecated: use deu_ros-srv:TwoInts-response instead.")))

(cl:ensure-generic-function 'result_add-val :lambda-list '(m))
(cl:defmethod result_add-val ((m <TwoInts-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deu_ros-srv:result_add-val is deprecated.  Use deu_ros-srv:result_add instead.")
  (result_add m))

(cl:ensure-generic-function 'result_mult-val :lambda-list '(m))
(cl:defmethod result_mult-val ((m <TwoInts-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deu_ros-srv:result_mult-val is deprecated.  Use deu_ros-srv:result_mult instead.")
  (result_mult m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TwoInts-response>) ostream)
  "Serializes a message object of type '<TwoInts-response>"
  (cl:let* ((signed (cl:slot-value msg 'result_add)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'result_mult)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TwoInts-response>) istream)
  "Deserializes a message object of type '<TwoInts-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result_add) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result_mult) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TwoInts-response>)))
  "Returns string type for a service object of type '<TwoInts-response>"
  "deu_ros/TwoIntsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TwoInts-response)))
  "Returns string type for a service object of type 'TwoInts-response"
  "deu_ros/TwoIntsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TwoInts-response>)))
  "Returns md5sum for a message object of type '<TwoInts-response>"
  "732182ffae20073c520fb831c7ee33cd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TwoInts-response)))
  "Returns md5sum for a message object of type 'TwoInts-response"
  "732182ffae20073c520fb831c7ee33cd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TwoInts-response>)))
  "Returns full string definition for message of type '<TwoInts-response>"
  (cl:format cl:nil "int64 result_add~%int64 result_mult~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TwoInts-response)))
  "Returns full string definition for message of type 'TwoInts-response"
  (cl:format cl:nil "int64 result_add~%int64 result_mult~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TwoInts-response>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TwoInts-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TwoInts-response
    (cl:cons ':result_add (result_add msg))
    (cl:cons ':result_mult (result_mult msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TwoInts)))
  'TwoInts-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TwoInts)))
  'TwoInts-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TwoInts)))
  "Returns string type for a service object of type '<TwoInts>"
  "deu_ros/TwoInts")