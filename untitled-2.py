# make an empty new list for use
  new_list = []
  # loop each message
  for msg_index in range(len(msg_list)):
      # get result by using the process_message function
      result = process_message(deck, msg_list[msg_index], crypt)
      # append the result obtained
      new_list.append(result)

  return new_list