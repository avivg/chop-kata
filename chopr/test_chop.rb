#!/usr/bin/env ruby

require 'test/unit'

module IterChop
  def chop(item, list)
    idx = list.index(item)
    idx.nil? ? -1 : idx
  end
end

class TestChop < Test::Unit::TestCase
  include IterChop

  def test_chop
    assert_equal 2, chop(3, [1,2,3,4,5])
    assert_equal  0, chop(1, [1, 2, 3, 4, 5])
    assert_equal -1, chop(6, [1, 2, 3, 4, 5])
    assert_equal  4, chop(5, [1, 2, 3, 4, 5])
    assert_equal  1, chop(2, [1, 2, 3, 4, 5])

    assert_equal  0, chop(2, [2, 3, 4, 5])
    assert_equal  1, chop(3, [2, 3, 4, 5])
    assert_equal  2, chop(4, [2, 3, 4, 5])
    assert_equal  3, chop(5, [2, 3, 4, 5])
    assert_equal -1, chop(1, [2, 3, 4, 5])

    assert_equal  0, chop(7, [7])
    assert_equal -1, chop(8, [7])

    assert_equal -1, chop(8, [])

    long_list = (0.upto 10000).to_a
    1000.times do |i|
        assert_equal i, chop(i, long_list)
    end
  end
end

