def response_by_corpus(chatbot, conversation):
    """
    A filter that eliminates possibly repetitive responses to prevent
    a chat bot from repeating statements that it has recently said.
    """
    #from collections import Counter

    # Get the most recent statements from the conversation
    conversation_statements = list(chatbot_bis.sql_storage.filter(
        conversation=conversation,
        tags='test'
    ))
    
    return (conversation_statements)
