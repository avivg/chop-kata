module IterChop
  def chop(item, list)
    start = 0
    stop = list.size - 1
    while start <= stop
      middle = ((start + stop) / 2).to_int
      middle_item = list[middle]
      if middle_item == item
        return middle
      end
      if middle_item < item
        start = middle + 1
      else
        stop = middle - 1
      end
    end
    return -1
  end
end
