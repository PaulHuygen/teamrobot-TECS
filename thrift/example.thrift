namespace java rise.core.utils.tecs
namespace py rise.core.utils.tecs

typedef i64 Time


# Names of the various messages #
# take care that string is case sensitive equal to structurename
################################
const string GetSpeechMsg = "GetSpeech"
const string SpeechMsg = "Speech"
const string GetVoiceCommandMsg = "GetVoiceCommand"
const string VoiceCommandMsg = "VoiceCommand"
const string SlideControlMsg = "SlideControlCommand"
const string XXXCommandMsg = "XXXCommand"
const string PollingMsg = "PollingData"
const string SpeechRecognitionCommandMsg = "SpeechRecognitionCommand"
const string PALToAll = ".*";
const string UserTextFeedbackMsg = "UserTextFeedback"
const string UserEmotionMsg = "UserEmotion"
const string QuizResponseMsg = "QuizResponse"
const string QuizCommandMsg = "QuizCommand"
const string QuizQuestionMsg = "QuizQuestion"
const string UserPictureMsg = "UserPicture"
const string DiaryFreeTextMsg = "DiaryFreeText"
const string UserSentimentMsg = "UserSentiment"
const string IntentionListMsg = "IntentionList"
const string IntentionMsg = "Intention"
const string DialogCommandMsg = "DialogCommand"
const string BehaviourMsg = "Behaviour"
const string LowLevelNaoCommandMsg = "LowLevelNaoCommand"
const string LowLevelExecuteCommandMsg = "LowLevelExecuteCommand"
const string SystemInfoMsg = "SystemInfo"
const string ChildActionMsg = "ChildAction"



# Names of the varios modules #
###############################
const string ActionSelector = "ActivitySelector";
const string NAOConnector = "NAOConnector";
const string ChildSimulator = "ChildSimulator";
const string BehaviorManager = "BehaviorManager";
const string Database = "Database";
const string SpeechRecognition = "SpeechRecognition";

# Messages related to the JSON structure to communicate with VU Amsterdam #
##################################
const string StructureMsg = "Structure"
const string MetadataMsg = "Metadata"
const string SemanticMsg = "Semantic"
const string EmotionsMsg = "Emotions"

# this message contains the data about structure
struct Structure{
	1:required i32 prepositional_phrases_count;
	2:required i32 adjective_count;
	3:required i32 non_future;
	4:required i32 active_sentences;
	5:required i32 personal_pronouns;
	6:required i32 word_length;
	7:required i32 negations;
	8:required i32 adverbs;
	9:required i32 passive_sentences;
	10:required i32 number_of_sentences;
	11:required i32 future;
	12:required i32 wordcount;
}

# this message contains the data about metadata
struct Metadata{
	1:required string speaker;
	2:required string lang;
	3:required string timestamp;
	4:required string input_text;
	5:required list<string> people_present;
	6:required string script_id; 
	7:required list<double> location_geometry_coordinates;
	8:required string location_geometry_type;
	9:required string location_type;
	10:required list<string> location_properties_name;
	11:required string scene_id; 
}

# this message contains the data about semantic
struct Semantic{
	1:required list<string> keywords;
	2:required list<string> organisations;
	3:required list<string> people;
	4:required list<string> places;
	5:required list<string> topics;
}

# this message contains the data about emotions
struct Emotions{
	1:required list<string> detected_emotion;
	2:required list<string> information_state;
}

const string RobotPresenterDataMsg = "RobotPresenterData"

# this message contains the data 
struct RobotPresenterData{
	1:required i32 structure_prepositional_phrases_count;
	2:required i32 structure_adjective_count;
	3:required i32 structure_non_future;
	4:required i32 structure_active_sentences;
	5:required i32 structure_personal_pronouns;
	6:required i32 structure_word_length;
	7:required i32 structure_negations;
	8:required i32 structure_adverbs;
	9:required i32 structure_passive_sentences;
	10:required i32 structure_number_of_sentences;
	11:required i32 structure_future;
	12:required i32 structure_wordcount;
	13:required string metadata_speaker;
	14:required string metadata_lang;
	15:required string metadata_timestamp;
	16:required string metadata_input_text;
	17:required string metadata_confidence_score;
	18:required list<string> metadata_other_possible_responses;
	19:required list<string> metadata_people_present;
	20:required string metadata_script_id; 
	21:required list<double> metadata_location_geometry_coordinates;
	22:required string metadata_location_geometry_type;
	23:required string metadata_location_type;
	24:required list<string> metadata_location_properties_name;
	25:required string metadata_scene_id; 
	26:required list<string> semantic_keywords;
	27:required list<string> semantic_organisations;
	28:required list<string> semantic_people;
	29:required list<string> semantic_places;
	30:required list<string> semantic_topics;
	31:required list<string> emotions_detected_emotion;
	32:required list<string> emotions_information_state;
}


const string ProcessedRobotPresenterDataMsg = "ProcessedRobotPresenterData"

# this message contains the data 
struct ProcessedRobotPresenterData{
	1:required i32 structure_prepositional_phrases_count;
	2:required i32 structure_adjective_count;
	3:required i32 structure_non_future;
	4:required i32 structure_active_sentences;
	5:required i32 structure_personal_pronouns;
	6:required i32 structure_word_length;
	7:required i32 structure_negations;
	8:required i32 structure_adverbs;
	9:required i32 structure_passive_sentences;
	10:required i32 structure_number_of_sentences;
	11:required i32 structure_future;
	12:required i32 structure_wordcount;
	13:required string metadata_speaker;
	14:required string metadata_lang;
	15:required string metadata_timestamp;
	16:required string metadata_input_text;
	17:required string metadata_confidence_score;
	18:required list<string> metadata_other_possible_responses;
	19:required list<string> metadata_people_present;
	20:required string metadata_script_id; 
	21:required list<double> metadata_location_geometry_coordinates;
	22:required string metadata_location_geometry_type;
	23:required string metadata_location_type;
	24:required list<string> metadata_location_properties_name;
	25:required string metadata_scene_id; 
	26:required list<string> semantic_keywords;
	27:required list<string> semantic_organisations;
	28:required list<string> semantic_people;
	29:required list<string> semantic_places;
	30:required list<string> semantic_topics;
	31:required list<string> emotions_detected_emotion;
	32:required list<string> emotions_information_state;
}


######################################

# this message contains the information needed to obtain Speech Recognition output(s)
struct GetSpeech{
	1:required i32 id;
	2:required i32 duration;
	3:required string language;
	4:required i32 alternatives;	
}

# this message contains Speech Recognition output(s)
struct Speech{
	1:required i32 id;
	2:required string results;
	3:required double confidence;
}

# this message contains the information needed to obtain Voice Command from ALSpeechRecognition
struct GetVoiceCommand{
	1:required i32 id;	
	2:required string language;
	3:required string word;
	4:required string threshold;	
}

# this message contains VoiceCommand output from ALSpeechRecognition
struct VoiceCommand{
	1:required i32 id;
	2:required string command;
	3:required double confidence;
}

struct PollingData{
	1:required i32 id;
	2:required string content;
}

struct SlideControlCommand{
	1:required i32 id;
	2:required i32 SlideNumber;
	3:optional string command;
}
struct XXXCommand {
	1:required i32 id;
	2:required string content;
}

struct SpeechRecognitionCommand {
	1:required i32 id;
	2:required string content;
}


# this message contains any system related message
struct SystemInfo {
	1:required i32 id;
	2:required string content;
}

# this message contains any message resulting from a child action on the tablet
struct ChildAction {
	1:required i32 id;
	2:required string content;
	3:required string childURI;
}

# Messages related to perception #
##################################

# this message contains any direct textual input coming from the child either through the SR or the interface
struct UserTextFeedback {
	1:required i32 id;
	2:required string content;
}

# this message contains emotional state information of the child. 
struct UserEmotion {
	1:required i32 id;
	2:required string content;
}

# this message contains the response of a child to a question
struct QuizResponse {
	1:required i32 id;
	2:required string category;
	3:required string questionText;
	4:required i32 response;  # 0-based!
	5:required bool correct;
}

struct UserPicture {
	1:required i32 id;
	2:required string content;
}

# this message contains a valence, arousal description of the child.
struct UserSentiment {
	1:required i32 id;
	2:required string content;
}

struct DiaryFreeText {
	1:required i32 id;
	2:required string content;
}

# Messages related to reasoning cycle #
#######################################

# this message contains a list of intentions which can be executed.  
struct IntentionList {
	1:required i32 id;
	2:required string content;
}

# this message contains the intention selected from the list
struct Intention {
	1:required i32 id;
	2:required string content;
	3:required double mood;
}

# Messages related to actions #
###############################

struct DialogCommand {
	1:required i32 id;
	2:required string content;
}

# this message contains command about the quiz
# [stop, start, question]
struct QuizCommand {
	1:required i32 id;
	2:required string command;
	3:required list<string> topics;
	4:required list<string> goals;
	5:required i32 level;
	6:required string asker; 	 # [child|robot]
}

# this message contains the data about a question
struct QuizQuestion {
	1:required i32 id;
	2:required string questionText;
	3:required list<string> answers;
	4:required string topic;
 	5:required i32 whichCorrect; # 0-based
	6:required string asker; 	 # [child|robot]
}

# this message contains the information needed to generate the behavior of the (virtual) NAO
struct Behaviour {
	1:required i32 id;
	2:required string gesture;
	3:required string textToSpeak;
	4:optional string type;
	5:optional double mood;
	6:optional i32 speechSpeed;
	7:optional double speechPitchShift;
	8:optional i32 speechShape;
	
}

# this message contains commands send to the NAO
# [startbehavior, stopbehavior, getposture, gotoposture]
struct LowLevelNaoCommand {
	1:required i32 id;
	2:required string command;
}

# this message contains the data for the joints values over time
struct LowLevelExecuteCommand {
	1:required i32 id;
	2:required list<string> joints;
	3:required list<list<double>> angles;
	4:required list<list<double>> times;
	5:required string textToSpeak
	6:required bool waitToConpleet
}


#
# Demo example
#

struct HelloWorldEvent {
	1:required string message = "HelloWorld";
}



service HWEService {
	string hello(1:string text);
}


