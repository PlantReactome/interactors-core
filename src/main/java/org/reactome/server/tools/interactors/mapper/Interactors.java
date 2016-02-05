package org.reactome.server.tools.interactors.mapper;

import java.util.List;

/**
 * Maps an Interaction in the JSON output
 *
 * @author Guilherme S Viteri <gviteri@ebi.ac.uk>
 */
@SuppressWarnings("unused")
public class Interactors {

    private String resource;

    private List<InteractorEntity> entities;

    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }

    public List<InteractorEntity> getEntities() {
        return entities;
    }

    public void setEntities(List<InteractorEntity> entities) {
        this.entities = entities;
    }

}