def traversal_list(ans,input_data,start,end,step) :
	for index in range(start,end,step):
		ans.append(input_data[index]);
	return ans;
def traversal_tuple(ans,input_data,start,end,step) :
	for index in range(start,end,step):
		ans +=(input_data[index],);
	return ans;

def traversal_set(ans,input_data,start,end,step) :
	ans.pop();
	for index in range(start,end,step):
		ans.add(input_data[index]);
	return ans;
def traversal_dict(ans,input_data,start,end,step) :
	for key,val in range(start,end,step).items():
		ans[key] = val;
	return ans;

def slice_op(input_data, start=0, end=None, step=1):
    if step == 0:
        return "Step cannot be zero"

    # Handle default end value
    if end is None:
        end = len(input_data)

    # Ensure start and end are within bounds
    if start < 0:
        start = max(0, len(input_data) + start)
    if end < 0:
        end = max(0, len(input_data) + end)
    end = min(end, len(input_data))

    # Process according to type
    if isinstance(input_data, list):
        return traversal_list([],input_data,start,end,step);
    elif isinstance(input_data, tuple):
        return traversal_tuple((),input_data,start,end,step);
    elif isinstance(input_data, set):
        # Convert to sorted list to maintain order for slicing
        sorted_list = sorted(input_data)
        return traversal_set({10,},sorted_list,start,end,step);
    elif isinstance(input_data, dict):
        # Return sliced list of keys
        return traversal_dict({},input_data,start,end,step);
    elif isinstance(input_data, str):
        return input_data[start:end:step]
    else:
        return "Unsupported type"

# Examples
print("List:", slice_op([10, 20, 30, 40], 1, 10))  # [20, 30, 40]
print("Tuple:", slice_op((10, 20, 30, 40), 1, 3))  # (20, 30)
print("Set:", slice_op({10, 20, 30, 40}, 1, 3))  # Set with sorted elements in range
print("Dict:", slice_op({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 1, 3))  # {'b': 2, 'c': 3}
print("String:", slice_op("abcdefghij", 2, 8, 2))  # "ceg"
