module RecursiveChop
  
  def rec_chop(item, list, start, stop)
    if start > stop
      return -1
    end
    middle = ((start + stop)/2).to_int
    middle_item = list[middle]
    if middle_item == item
      return middle
    end
    if middle_item < item
      rec_chop(item, list, middle + 1, stop)
    else
      rec_chop(item, list, start, middle - 1)
    end
  end

  def chop(item, list)
    start = 0
    stop = list.size - 1
    rec_chop(item, list, start, stop)
  end

end
