module RecursiveChop
  def chop(item, list)
    idx = list.index(item)
    idx.nil? ? -1 : idx
  end
end
