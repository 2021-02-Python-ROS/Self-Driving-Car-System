;; Auto-generated. Do not edit!


(when (boundp 'deu_ros::TwoInts)
  (if (not (find-package "DEU_ROS"))
    (make-package "DEU_ROS"))
  (shadow 'TwoInts (find-package "DEU_ROS")))
(unless (find-package "DEU_ROS::TWOINTS")
  (make-package "DEU_ROS::TWOINTS"))
(unless (find-package "DEU_ROS::TWOINTSREQUEST")
  (make-package "DEU_ROS::TWOINTSREQUEST"))
(unless (find-package "DEU_ROS::TWOINTSRESPONSE")
  (make-package "DEU_ROS::TWOINTSRESPONSE"))

(in-package "ROS")





(defclass deu_ros::TwoIntsRequest
  :super ros::object
  :slots (_a _b ))

(defmethod deu_ros::TwoIntsRequest
  (:init
   (&key
    ((:a __a) 0)
    ((:b __b) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   (setq _b (round __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; int32 _a
    4
    ;; int32 _b
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _a
       (write-long _a s)
     ;; int32 _b
       (write-long _b s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _a
     (setq _a (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _b
     (setq _b (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass deu_ros::TwoIntsResponse
  :super ros::object
  :slots (_result_add _result_mult ))

(defmethod deu_ros::TwoIntsResponse
  (:init
   (&key
    ((:result_add __result_add) 0)
    ((:result_mult __result_mult) 0)
    )
   (send-super :init)
   (setq _result_add (round __result_add))
   (setq _result_mult (round __result_mult))
   self)
  (:result_add
   (&optional __result_add)
   (if __result_add (setq _result_add __result_add)) _result_add)
  (:result_mult
   (&optional __result_mult)
   (if __result_mult (setq _result_mult __result_mult)) _result_mult)
  (:serialization-length
   ()
   (+
    ;; int64 _result_add
    8
    ;; int64 _result_mult
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _result_add
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _result_add (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _result_add) (= (length (_result_add . bv)) 2)) ;; bignum
              (write-long (ash (elt (_result_add . bv) 0) 0) s)
              (write-long (ash (elt (_result_add . bv) 1) -1) s))
             ((and (class _result_add) (= (length (_result_add . bv)) 1)) ;; big1
              (write-long (elt (_result_add . bv) 0) s)
              (write-long (if (>= _result_add 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _result_add s)(write-long (if (>= _result_add 0) 0 #xffffffff) s)))
     ;; int64 _result_mult
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _result_mult (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _result_mult) (= (length (_result_mult . bv)) 2)) ;; bignum
              (write-long (ash (elt (_result_mult . bv) 0) 0) s)
              (write-long (ash (elt (_result_mult . bv) 1) -1) s))
             ((and (class _result_mult) (= (length (_result_mult . bv)) 1)) ;; big1
              (write-long (elt (_result_mult . bv) 0) s)
              (write-long (if (>= _result_mult 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _result_mult s)(write-long (if (>= _result_mult 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _result_add
#+(or :alpha :irix6 :x86_64)
      (setf _result_add (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _result_add (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _result_mult
#+(or :alpha :irix6 :x86_64)
      (setf _result_mult (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _result_mult (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass deu_ros::TwoInts
  :super ros::object
  :slots ())

(setf (get deu_ros::TwoInts :md5sum-) "732182ffae20073c520fb831c7ee33cd")
(setf (get deu_ros::TwoInts :datatype-) "deu_ros/TwoInts")
(setf (get deu_ros::TwoInts :request) deu_ros::TwoIntsRequest)
(setf (get deu_ros::TwoInts :response) deu_ros::TwoIntsResponse)

(defmethod deu_ros::TwoIntsRequest
  (:response () (instance deu_ros::TwoIntsResponse :init)))

(setf (get deu_ros::TwoIntsRequest :md5sum-) "732182ffae20073c520fb831c7ee33cd")
(setf (get deu_ros::TwoIntsRequest :datatype-) "deu_ros/TwoIntsRequest")
(setf (get deu_ros::TwoIntsRequest :definition-)
      "int32 a
int32 b
---
int64 result_add
int64 result_mult

")

(setf (get deu_ros::TwoIntsResponse :md5sum-) "732182ffae20073c520fb831c7ee33cd")
(setf (get deu_ros::TwoIntsResponse :datatype-) "deu_ros/TwoIntsResponse")
(setf (get deu_ros::TwoIntsResponse :definition-)
      "int32 a
int32 b
---
int64 result_add
int64 result_mult

")



(provide :deu_ros/TwoInts "732182ffae20073c520fb831c7ee33cd")


