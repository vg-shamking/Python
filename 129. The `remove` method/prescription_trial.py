from prescription_data import *
import colorama

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)  # KeyError: ('Warfarin', 'anti-coagulant') for Kenny
        prescription.add(edoxaban)
    except KeyError:
        # print('\u001b[31m', '\u001b[4m')  # for fun ^_^
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial.")
    print(patient, prescription)
    # print('\u001b[0m')
# print("Normal text")
