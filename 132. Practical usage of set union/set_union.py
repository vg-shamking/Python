from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interaction)
    # meds_to_watch = meds_to_watch | interaction
    # meds_to_watch.update(interaction)
    # meds_to_watch |= interaction  # same results

# meds_to_watch.update(adverse_interactions[0],
#                      adverse_interactions[1],
#                      adverse_interactions[2],
#                      adverse_interactions[3],
#                      adverse_interactions[4],
#                      adverse_interactions[5],
#                      adverse_interactions[6])
# only demonstration - never use this code
# it will crush in case less than 7 elements
# change it all with one line:
meds_to_watch.update(*adverse_interactions)

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')
