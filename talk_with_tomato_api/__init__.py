from chatterbot import ChatBot
from chatterbot.comparisons import levenshtein_distance, jaccard_similarity, sentiment_comparison, synset_distance
from chatterbot.response_selection import get_first_response

msg_id=0
bot = ChatBot(
	'Tomato',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	database_uri='sqlite:///update_corpus_database.sqlite3',

	preprocessors=[
		'chatterbot.preprocessors.clean_whitespace'
	],

	logic_adapters=[
		{
			"import_path": "chatterbot.logic.BestMatch",
			"statement_comparison_function": levenshtein_distance,
			"statement_comparison_function": synset_distance,
			"response_selection_method": get_first_response,
			'default_response': 'I am sorry, but I do not understand.',
			'maximum_similarity_threshold': 0.50
		},
{
			"import_path": "chatterbot.logic.BestMatch",
			"statement_comparison_function": jaccard_similarity,
			"statement_comparison_function": levenshtein_distance,
			"statement_comparison_function": sentiment_comparison,
			"response_selection_method": get_first_response,
			'default_response': 'I am sorry, but I do not understand.',
			'maximum_similarity_threshold': 0.50
		},
		{

			"import_path": "chatterbot.logic.MathematicalEvaluation",
		}
	],)