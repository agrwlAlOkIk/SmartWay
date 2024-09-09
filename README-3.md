
SmartWay - AI-Powered Traffic Flow Optimization System

SmartWay is an AI-based solution that optimizes traffic flow at intersections by analyzing real-time traffic congestion and dynamically adjusting traffic light timings. The system assigns a traffic rating from 1 to 10, adjusts the signal timings accordingly, and balances traffic flow between intersections for better efficiency and reduced wait times.

Table of Contents

	1.	Features
	2.	Technology Stack
	3.	System Architecture
	4.	Installation
	5.	Usage
	6.	Folder Structure
	7.	Contributing
	8.	License

Features

	•	Real-Time Traffic Detection: Analyze traffic using video feeds or simulated video inputs.
	•	Dynamic Traffic Rating: Assign a rating (1-10) to intersections based on congestion levels.
	•	Adaptive Traffic Light Timings: Automatically reduce or increase signal timings based on congestion at each signal.
	•	Cross-Intersection Coordination: Ensure smoother traffic flow by adjusting timings across multiple intersections.
	•	Visual Traffic Monitoring: View real-time traffic ratings and signal statuses on an interactive dashboard.

Technology Stack

Frontend:

	•	React: For building the interactive user interface.
	•	Axios: To communicate with the backend API.
	•	WebSockets: To display real-time traffic data and signal status.

Backend:

	•	Node.js + Express.js: For building the REST API and handling backend logic.
	•	Python (OpenCV/YOLO): For detecting and analyzing traffic congestion from video feeds.
	•	MongoDB/PostgreSQL: For storing traffic data, congestion levels, and signal timings.

Infrastructure:

	•	Turborepo: For monorepo management, integrating both JavaScript (Express, React) and Python services.
	•	Redis (optional): For handling real-time communication between services or caching data.

System Architecture

	1.	Frontend (React):
	•	Dashboard that displays traffic congestion levels, ratings (1-10), and signal statuses.
	•	WebSocket integration for real-time updates.
	2.	Backend (Express.js):
	•	REST API that receives video data or simulation data from frontend.
	•	Sends video data to Python service for processing.
	•	Adjusts signal timings based on traffic ratings.
	3.	Python (OpenCV/YOLO):
	•	Processes video data to detect vehicles and analyze traffic congestion.
	•	Returns congestion levels and traffic ratings to the Express.js backend.
	4.	Database (MongoDB/PostgreSQL):
	•	Stores traffic data, signal timings, and intersection statuses for analysis and historical tracking.
	5.	Signal Timing Controller:
	•	Adjusts traffic light timings based on congestion data, optimizing flow across multiple intersections.




