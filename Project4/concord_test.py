from hash_lin_table import *
import filecmp

# Create stop words hash table
# start with table size of 251, grow as needed
stop_words = HashTableLinPr(251)
# read in stop words, load hash table
stop_words.read_stop('stop_words.txt')

# Create concordance hash table
# start with table size of 251, grow as needed
concord = HashTableLinPr(251)
# read from file, process as required, load hash table
concord.read_file('input1.txt', stop_words)
concord.save_concordance('test1.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
# will be True if files match#
print("File compare:", filecmp.cmp('test1.txt', 'input1_sol.txt'))
# Create concordance hash table
# start with table size of 251, grow as needed
concord = HashTableLinPr(251)
# read from file, process as required, load hash table
concord.read_file('input2.txt', stop_words)
concord.save_concordance('test2.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
# will be True if files match
print("File compare:", filecmp.cmp('test2.txt', 'input2_sol.txt'))

from hash_quad_table import *

# Create stop words hash table
# start with table size of 251, grow as needed
stop_words = HashTableQuadPr(251)
# read in stop words, load hash table
stop_words.read_stop('stop_words.txt')

# Create concordance hash table
# start with table size of 251, grow as needed
concord = HashTableLinPr(251)
# read from file, process as required, load hash table
concord.read_file('input1.txt', stop_words)
concord.save_concordance('qtest1.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
# will be True if files match#
print("File compare:", filecmp.cmp('qtest1.txt', 'input1_sol.txt'))
# Create concordance hash table
# start with table size of 251, grow as needed
concord = HashTableQuadPr(251)
# read from file, process as required, load hash table
concord.read_file('input2.txt', stop_words)
concord.save_concordance('qtest2.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
# will be True if files match
print("File compare:", filecmp.cmp('qtest2.txt', 'input2_sol.txt'))
