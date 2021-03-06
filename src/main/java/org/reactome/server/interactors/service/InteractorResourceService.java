package org.reactome.server.interactors.service;

import org.reactome.server.interactors.dao.InteractorResourceDAO;
import org.reactome.server.interactors.dao.intact.StaticInteractorResource;
import org.reactome.server.interactors.database.InteractorsDatabase;
import org.reactome.server.interactors.model.InteractorResource;

import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * @author Guilherme S Viteri <gviteri@ebi.ac.uk>
 */

public class InteractorResourceService {

    private InteractorResourceDAO interactorResourceDao;

    public InteractorResourceService(InteractorsDatabase database){
        interactorResourceDao = new StaticInteractorResource(database);
    }

    /**
     * Retrieves all Interactor Resources from database
     * @throws SQLException
     */
    public List<InteractorResource> getAll() throws SQLException {
        return interactorResourceDao.getAll();
    }

    /**
     * Retrieve all interactor resource into a Map data structure having
     * the unique db id as the key
     *
     * @throws SQLException
     */
    public Map<Long, InteractorResource> getAllMappedById() throws SQLException {
        Map<Long, InteractorResource> interactorResourceMap = new HashMap<>();
        List<InteractorResource> interactorResourceList = interactorResourceDao.getAll();
        for (InteractorResource interactorResource : interactorResourceList) {
            interactorResourceMap.put(interactorResource.getId(), interactorResource);
        }

        return interactorResourceMap;
    }

    /**
     * Retrieve all interactor resource into a Map data structure having
     * the name as the key
     * @throws SQLException
     */
    public Map<String, InteractorResource> getAllMappedByName() throws SQLException {
        Map<String, InteractorResource> interactorResourceMap = new HashMap<>();
        List<InteractorResource> interactorResourceList = interactorResourceDao.getAll();
        for (InteractorResource interactorResource : interactorResourceList) {
            interactorResourceMap.put(interactorResource.getName(), interactorResource);
        }

        return interactorResourceMap;
    }
    
}
