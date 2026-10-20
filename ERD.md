erDiagram
    SETTINGS ||--o{ SESSION : configures
    SESSION ||--o{ MESSAGE : contains
    SESSION ||--o{ RECOGNITION_RESULT : logs
    SESSION ||--o{ ERROR_LOG : records
    MESSAGE ||--o{ MESSAGE_SIGN : "is made of"
    SIGN ||--o{ MESSAGE_SIGN : "appears in"
    SIGN ||--o| SIGN_ANIMATION : has
    SIGN ||--o{ SIGN_SAMPLE : "trained on"
    SIGN |o--o{ RECOGNITION_RESULT : "predicted as"
    ML_MODEL ||--o{ RECOGNITION_RESULT : produces
    MESSAGE |o--o{ RECOGNITION_RESULT : yields
    MESSAGE ||--o| SPEECH_INPUT : "may have"
    MESSAGE ||--o| SPEECH_OUTPUT : "may have"
    MESSAGE ||--o{ ANIMATION_PLAYBACK : "displayed as"
    SIGN_ANIMATION ||--o{ ANIMATION_PLAYBACK : "played in"
    ERROR_TYPE ||--o{ ERROR_LOG : classifies
    MESSAGE |o--o{ ERROR_LOG : "may cause"

    SETTINGS {
        int settings_id PK
        string default_output_mode
        string default_input_mode
        boolean tts_enabled
        int speech_rate
        float avatar_speed
        datetime updated_at
    }
    SESSION {
        int session_id PK
        int settings_id FK
        string camera_permission_status
        string output_mode
        string input_mode
        string status
        datetime started_at
        datetime ended_at
    }
    MESSAGE {
        int message_id PK
        int session_id FK
        string sender_role
        string direction
        string input_type
        string text_content
        datetime created_at
    }
    SIGN {
        int sign_id PK
        string gloss UK
        string category
        string description
        boolean is_supported
    }
    MESSAGE_SIGN {
        int message_sign_id PK
        int message_id FK
        int sign_id FK
        int sequence_position
    }
    SIGN_ANIMATION {
        int animation_id PK
        int sign_id FK
        string glb_file_path
        string clip_name
        int duration_ms
    }
    SIGN_SAMPLE {
        int sample_id PK
        int sign_id FK
        string source
        string landmark_file_path
        string data_split
    }
    ML_MODEL {
        int model_id PK
        string name
        string algorithm
        string version
        int vocabulary_size
        float accuracy
        string file_path
        boolean is_active
        datetime trained_at
    }
    RECOGNITION_RESULT {
        int result_id PK
        int session_id FK
        int model_id FK
        int sign_id FK
        int message_id FK
        float confidence
        string status
        datetime recognized_at
    }
    SPEECH_INPUT {
        int speech_input_id PK
        int message_id FK
        string audio_path
        string converted_text
        string status
    }
    SPEECH_OUTPUT {
        int speech_output_id PK
        int message_id FK
        string engine
        string audio_path
        datetime generated_at
    }
    ANIMATION_PLAYBACK {
        int playback_id PK
        int message_id FK
        int animation_id FK
        boolean is_replay
        datetime played_at
    }
    ERROR_TYPE {
        int error_type_id PK
        string error_code UK
        string description
        string detection_point
        string fallback_action
        string user_message
    }
    ERROR_LOG {
        int error_id PK
        int session_id FK
        int message_id FK
        int error_type_id FK
        string outcome
        datetime occurred_at
    }<img width="2368" height="2214" alt="EDG" src="https://github.com/user-attachments/assets/9ea10737-cc6a-4ffd-972e-427068b804d7" />
