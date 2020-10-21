from timeit import default_timer as timer
from Processing.TractPopulationChangeSummarizer import TractPopulationChangeSummarizer

start = timer()

print(f'Process started')

TractPopulationChangeSummarizer().summarize_data_set()

end = timer()
elapsed_time = (end - start) * 1000

print(f'Process ended in {elapsed_time} milliseconds')
