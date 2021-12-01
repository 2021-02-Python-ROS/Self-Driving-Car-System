
(cl:in-package :asdf)

(defsystem "deu_ros-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TwoInts" :depends-on ("_package_TwoInts"))
    (:file "_package_TwoInts" :depends-on ("_package"))
    (:file "WordCount" :depends-on ("_package_WordCount"))
    (:file "_package_WordCount" :depends-on ("_package"))
  ))