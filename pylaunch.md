# Pylaunch

## Domain Views

```mermaid
graph LR
	script{Script}
	user -- triggers --> syntaxCheck -- in --> editor
	user -- checks --> errorModal -- in --> editor
	user -- navigates using --> toolbar -- to --> page{Page}
	subgraph User
        user -- stores --> s1{script}
        user -- loads --> script
        user -- runs --> s2{script} -- shows result --> window -- to --> user
        user -- creates new --> script
        user -- edits --> s3{script} -- in --> editor{Editor}
	    user -- edits --> configfile
        user -- stores --> configfile{Configfile}
	end
```

As an User I want to edit python scripts to modify their source code.
As an User I want to execute my python scripts to automate and interact with my programs.
As an User I want to store (disk) and download (cloud) my scripts anytime without hassle.
As an User I want to update the program without thinking about it.

```mermaid
graph LR
	subgraph App
        app2(app) -- holds --> list -- of --> script{Script}
        configfile{Configfile} -- setups --> app1(app)
        script -- stores to --> disk & cloud
	end
```

```mermaid
graph LR
    subgraph Script
        script -- executes --> sourcecode
    end
```

```mermaid
graph LR
	subgraph Editor
		syntaxCheck(syntax check) -- validates --> script{Script}
		errorModal(error modal) -- shows fails of --> script
		runner -- executes --> script
	end
```

```mermaid
graph LR
	subgraph Frame
		app -- includes --> frame -- includes --> p1
	end
	subgraph Page
		p1(page) -- includes --> fragment/s -- hold --> component/s
	end
```

```mermaid
graph LR
	subgraph Configfile
		format -- uses --> json
	end
```



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

## Project Assets

#### Links

https://coolors.co/1500ff-007bff-00eeff-00ffcb-00ff5d