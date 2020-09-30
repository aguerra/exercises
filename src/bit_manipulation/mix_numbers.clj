(ns bit-manipulation.mix-numbers
  (:require [clojure.test :refer :all]))

(defn mix-numbers
  "You are given two numbers, x and y, and two bit positions, i and j.
  Write a method to insert y into x such that y starts at bit j and
  ends at bit n. You can assume that the bits j through n have enough
  space to fit all of y."
  [x y n j]
  (let [right-ones (dec (bit-shift-left 1 n))
        shifted    (bit-shift-left y n)]
    (-> (bit-not 0)
        (bit-shift-left (inc j))
        (bit-or right-ones)
        (bit-and x)
        (bit-or shifted))))

(deftest tests
  (are [x y n j r] (= r (mix-numbers x y n j))
    2r000001      2r11     2 4  2r001101
    2r10000000000 2r10011  2 6  2r10001001100
    2r111110100   2r100001 3 8  2r100001100))

(run-tests)
