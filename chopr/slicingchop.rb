
module SliceChop
  def chop(item, list, start = 0)
    if list.empty?
      return -1
    else
      middle = list.size / 2
      middle_item = list[middle]
      base = middle + start
      if middle_item == item
        return base
      end
      if middle_item < item
        chop(item, list[(middle + 1) .. -1], base + 1)
      else
        chop(item, list[0 ... middle], start)
      end
    end
  end
end
