# Pylaunch

## Domain Views

```mermaid
graph LR
	user -- triggers --> syntaxCheck
	user -- checks --> errorModal
	user -- navigates using --> toolbar -- to --> fragment
	subgraph App
        app -- holds --> list -- of --> script
        configfile -- setups --> app
	end
	subgraph User
        user -- stores --> s1("script") -- to --> disk & cloud
        user -- loads --> script
        user -- runs --> s2("script") -- shows result --> window -- to --> user
        user -- creates new --> script
        user -- edits --> s3("script") -- in --> editor
        
	end
	subgraph Developer
        developer -- edits --> configfile
        developer -- stores --> cf1("configfile") -- as --> json
	end
	subgraph Script
		script -- executes --> sourcecode
	end
	subgraph Editor
		syntaxCheck(syntax check) -- validates --> script
		errorModal(error modal) -- shows fails of --> script
	end
	subgraph Page
		fragment -- holds --> page
	end
```

As an User I want to edit python scripts to modify their source code.
As an User I want to execute my python scripts to automate and interact with my programs.
As an User I want to store (disk) and download (cloud) my scripts anytime without hassle.
As an User I want to update the program without thinking about it.

## Technical Views

````mermaid
graph TD
	bf --> bb --> bf
	eb --- ef
	state -- used by --> components
	components -- store global data into --> state
	
	subgraph Frontend
		ef("eel")
		bf("bridge")
		components
	end

	subgraph Backend
		eb("eel")
		bb("bridge")
	end
	
	subgraph Store
		state
	end
````

