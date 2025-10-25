# API Documentation - HR AI System

## 🔌 **Base URL**
```
http://localhost:5000
```

## 📋 **Endpoints**

### **GET /** - Health Check
**Description**: Check if the API is running and RL Agent is initialized

**Request:**
```bash
curl http://localhost:5000/
```

**Response:**
```json
"HR RL Agent Backend Running (Self-Automation Enabled)"
```

**Status Codes:**
- `200`: API is running
- `500`: Server error

---

### **POST /update_feedback** - Submit HR Feedback
**Description**: Submit feedback for a candidate-job pair to train the RL agent

**Request:**
```bash
curl -X POST http://localhost:5000/update_feedback \
  -H "Content-Type: application/json" \
  -d '{
    "candidate_id": 1,
    "jd_id": 1,
    "feedback_score": 4,
    "comment": "Excellent technical skills and team fit"
  }'
```

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `candidate_id` | integer | Yes | ID of the candidate (1-100) |
| `jd_id` | integer | Yes | ID of the job description (1-10) |
| `feedback_score` | integer | Yes | Score from -1 to 5 |
| `comment` | string | Yes | HR feedback comment |

**Response:**
```json
{
  "status": "updated_and_logged",
  "candidate_id": 1,
  "jd_id": 1,
  "rl_policy_change": "System now suggests 'accept'",
  "feedback_summary": "Excellent technical skills and team fit"
}
```

**Response Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Processing status |
| `candidate_id` | integer | Processed candidate ID |
| `jd_id` | integer | Processed job ID |
| `rl_policy_change` | string | New RL agent recommendation |
| `feedback_summary` | string | AI-generated summary (if Gemini enabled) |

**Status Codes:**
- `200`: Feedback processed successfully
- `400`: Invalid request data
- `500`: Server error or RL Agent not initialized

**Error Response:**
```json
{
  "status": "error",
  "message": "Missing required fields"
}
```

## 🧪 **Testing Examples**

### **Python Example:**
```python
import requests

# Health check
response = requests.get('http://localhost:5000/')
print(response.text)

# Submit feedback
feedback_data = {
    "candidate_id": 1,
    "jd_id": 1,
    "feedback_score": 4,
    "comment": "Strong technical background and good communication skills"
}

response = requests.post(
    'http://localhost:5000/update_feedback',
    json=feedback_data
)

print(response.json())
```

### **JavaScript Example:**
```javascript
// Health check
fetch('http://localhost:5000/')
  .then(response => response.text())
  .then(data => console.log(data));

// Submit feedback
const feedbackData = {
  candidate_id: 1,
  jd_id: 1,
  feedback_score: 4,
  comment: "Excellent candidate with relevant experience"
};

fetch('http://localhost:5000/update_feedback', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(feedbackData)
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🔧 **Integration Guide**

### **HRIS Integration:**
```python
class HRISIntegration:
    def __init__(self, api_base_url="http://localhost:5000"):
        self.base_url = api_base_url
    
    def submit_feedback(self, candidate_id, job_id, score, comment):
        response = requests.post(
            f"{self.base_url}/update_feedback",
            json={
                "candidate_id": candidate_id,
                "jd_id": job_id,
                "feedback_score": score,
                "comment": comment
            }
        )
        return response.json()
```

### **Webhook Integration:**
```python
# Example webhook receiver
@app.route('/webhook/feedback', methods=['POST'])
def receive_feedback():
    data = request.json
    
    # Forward to HR AI System
    response = requests.post(
        'http://localhost:5000/update_feedback',
        json=data
    )
    
    return response.json()
```

## 📊 **Rate Limits**
- No rate limits in development
- Production: 100 requests/minute per IP

## 🔐 **Authentication**
- Development: No authentication required
- Production: Implement API key authentication

## 📝 **Data Models**

### **Candidate Data:**
- IDs: 1-100
- Fields: name, education, experience_years, skills, location

### **Job Description Data:**
- IDs: 1-10
- Fields: title, description

### **Feedback Scores:**
- `-1`: Very poor fit
- `0`: Poor fit
- `1`: Below average
- `2`: Average
- `3`: Above average
- `4`: Good fit
- `5`: Excellent fit