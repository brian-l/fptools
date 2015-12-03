if __name__ == "__main__":

    from fptools import *
    from operator import add

    def test_finite(func, iterations = 10):
        return [next(func) for x in xrange(iterations)]

    counting = count()
    print "count from 0 to 10:\n\t", test_finite(counting, iterations = 11)

    repeating = repeat(5)
    print "repeat 5 ten times:\n\t", test_finite(repeating)

    seq = range(5)

    cycles = cycle(seq)
    print "cycling 12 items from %s:\n\t" % seq, test_finite(cycles, iterations = 12)

    seq_left = range(5)
    seq_right = range(10, 15)
    zipped = zip_with(add, *[seq_left, seq_right])
    print "adding %s to %s:\n\t" % (seq_left, seq_right), test_finite(zipped, iterations = 5)

    to_part = range(8)
    parted = partition(to_part, 3)
    print "partitioning %s into chunks of 3:\n\t" % to_part, list(parted)

    first = head(seq)
    print "lazy first item in %s:\n\t" % seq, first

    end = last(seq)
    print "lazy last item in %s:\n\t" % seq, end

    tail_ = tail(seq)
    print "lazy tail in %s:\n\t" % seq, list(tail_)

    # init_ = init(seq)
    # print "lazy init in %s" % seq, list(init_)

