#!/usr/bin/env ruby

require 'test/unit'

module TestChop
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


require_relative 'iterativechop'
class TestIterChop < Test::Unit::TestCase
  include IterChop
  include TestChop
end

require_relative 'recursivechop'
class TestRecursiveChop < Test::Unit::TestCase
  include RecursiveChop
  include TestChop
end

require_relative 'oochop'
class TestOOChop < Test::Unit::TestCase
  include OOChop
  include TestChop
end

require_relative 'slicingchop'
class TestSliceChop < Test::Unit::TestCase
  include SliceChop
  include TestChop
end
