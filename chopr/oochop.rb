module OOChop

  class Finder
    def initialize(list, start = 0, stop = nil)
      @list = list
      @start = start
      @stop = stop.nil? ? list.size - 1 : stop
      if @start > @stop
        @finder = lambda {|x| -1 }
      else
        @finder = lambda {|x| find_in_non_empty_list(x)}
      end
    end

    def find(item)
      @finder.call(item)
    end

    def find_in_non_empty_list(item)
      # return @list.index(item).nil? ? -1 : @list.index(item)
      middle = (@start + @stop) / 2
      middle_item = @list[middle]
      if middle_item == item
        return middle
      end
      if middle_item > item
        Finder.new(@list, @start, middle - 1).find(item)
      else
        Finder.new(@list, middle + 1, @stop).find(item)
      end
    end
  end

  def chop(item, list)
    Finder.new(list).find(item)
  end
end