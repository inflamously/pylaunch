# Pylaunch

## Domain Views

```mermaid
graph LR
	subgraph App
        app -- holds --> list -- of --> script
        configfile -- setups --> app
	end
	subgraph User
        user -- stores --> s1("script") -- to --> disk
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
	
	subgraph Frontend
		ef("eel")
		bf("bridge")
		components -- store global data into --> state
		state -- used by --> components
	end

	subgraph Backend
		eb("eel")
		bb("bridge")
	end
	
	subgraph Store
		state
	end
````

